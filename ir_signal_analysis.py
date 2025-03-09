import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 定义RNN模型
class IRSignalRNN(nn.Module):
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, num_classes=2):
        super(IRSignalRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.dropout = nn.Dropout(0.2)
        self.fc = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        # 初始化隐藏状态
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # LSTM前向传播
        out, _ = self.lstm(x, (h0, c0))
        out = self.dropout(out[:, -1, :])  # 取最后一个时间步的输出
        out = self.fc(out)
        return out

# 自定义数据集类
class IRSignalDataset(Dataset):
    def __init__(self, sequences, labels):
        self.sequences = torch.FloatTensor(sequences)
        self.labels = torch.LongTensor(labels)
    
    def __len__(self):
        return len(self.sequences)
    
    def __getitem__(self, idx):
        return self.sequences[idx], self.labels[idx]

# 读取数据
df = pd.read_csv('digital.csv')
level_data = df.iloc[:, 1].values

# 找到所有高电平段
high_level_segments = []
current_segment = []
for i, level in enumerate(level_data):
    if level == 1:
        current_segment.append(i)
    elif current_segment:
        if len(current_segment) > 1:  # 只保留长度大于1的段
            high_level_segments.append(current_segment)
        current_segment = []

# 提取每个高电平段的长度
segment_lengths = [len(segment) for segment in high_level_segments]

# 数据预处理
X = np.array(segment_lengths).reshape(-1, 1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 创建序列数据
sequence_length = 5
sequences = []
for i in range(len(X_scaled) - sequence_length):
    sequences.append(X_scaled[i:i+sequence_length])

# 使用K-means聚类来初步区分引导码和数据码
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X.reshape(-1, 1))

# 计算数据码的短码和长码平均值
data_code_lengths = X[clusters == 1]  # 假设cluster 1为数据码
short_codes = data_code_lengths[data_code_lengths < np.median(data_code_lengths)]
long_codes = data_code_lengths[data_code_lengths >= np.median(data_code_lengths)]

# 创建标签数据（使用kmeans的结果作为初始标签）
labels = clusters[sequence_length:]  # 确保标签长度与序列数据匹配
labels = torch.LongTensor(labels)

# 重新创建数据集和数据加载器
dataset = IRSignalDataset(sequences, labels)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 训练参数
num_epochs = 50
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = IRSignalRNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 训练循环
print("\n开始训练模型...")
model.train()
for epoch in range(num_epochs):
    total_loss = 0
    correct = 0
    total = 0
    
    for batch_idx, (data, target) in enumerate(dataloader):
        # 将数据移到设备（GPU/CPU）
        data = data.to(device)
        target = target.to(device)
        
        # 前向传播
        outputs = model(data)
        loss = criterion(outputs, target)
        
        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # 统计
        total_loss += loss.item()
        _, predicted = outputs.max(1)
        total += target.size(0)
        correct += predicted.eq(target).sum().item()
        
    # 打印每个epoch的统计信息
    avg_loss = total_loss / len(dataloader)
    accuracy = 100. * correct / total
    if (epoch + 1) % 5 == 0:  # 每5个epoch打印一次
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}, Accuracy: {accuracy:.2f}%')

print("模型训练完成！")

# 模型评估
model.eval()
with torch.no_grad():
    all_predictions = []
    for data, _ in dataloader:
        data = data.to(device)
        outputs = model(data)
        _, predicted = outputs.max(1)
        all_predictions.extend(predicted.cpu().numpy())

# 使用训练后的模型预测结果
predictions = np.array(all_predictions)
data_code_lengths_rnn = X[sequence_length:][predictions == 1]  # 使用RNN预测的数据码
short_codes_rnn = data_code_lengths_rnn[data_code_lengths_rnn < np.median(data_code_lengths_rnn)]
long_codes_rnn = data_code_lengths_rnn[data_code_lengths_rnn >= np.median(data_code_lengths_rnn)]

# 打印分析结果
print("\n分析结果：")
print("K-means聚类结果：")
print(f"引导码平均长度: {np.mean(X[clusters == 0]):.2f}")
print(f"数据码短码平均值: {np.mean(short_codes):.2f}")
print(f"数据码长码平均值: {np.mean(long_codes):.2f}")

print("\nRNN模型分析结果：")
print(f"引导码平均长度: {np.mean(X[sequence_length:][predictions == 0]):.2f}")
print(f"数据码短码平均值: {np.mean(short_codes_rnn):.2f}")
print(f"数据码长码平均值: {np.mean(long_codes_rnn):.2f}")

# 保存结果到文件
with open('analysis_results.txt', 'w', encoding='utf-8') as f:
    f.write("红外信号分析结果\n")
    f.write("-----------------\n")
    f.write("\nK-means聚类结果：\n")
    f.write(f"引导码平均长度: {np.mean(X[clusters == 0]):.2f}\n")
    f.write(f"数据码短码平均值: {np.mean(short_codes):.2f}\n")
    f.write(f"数据码长码平均值: {np.mean(long_codes):.2f}\n")
    
    f.write("\nRNN模型分析结果：\n")
    f.write(f"引导码平均长度: {np.mean(X[sequence_length:][predictions == 0]):.2f}\n")
    f.write(f"数据码短码平均值: {np.mean(short_codes_rnn):.2f}\n")
    f.write(f"数据码长码平均值: {np.mean(long_codes_rnn):.2f}\n")

# 保存训练好的模型
torch.save(model.state_dict(), 'ir_signal_model.pth') 
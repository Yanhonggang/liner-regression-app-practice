import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# 生成一些随机数据来训练模型
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 创建和训练线性回归模型
model = LinearRegression()
model.fit(X, y)

# 保存模型
joblib.dump(model, 'backend/linear_regression_model.pkl')

print("model saved")

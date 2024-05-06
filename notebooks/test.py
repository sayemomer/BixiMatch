import numpy as np

# Suppose these are feature arrays where each array has the same number of samples (rows)
feature1 = np.random.rand(10, 1)  # 10 samples, 1 feature
feature2 = np.random.rand(10, 2)  # 10 samples, 2 features
feature3 = np.random.rand(10, 1)  # 10 samples, 1 feature

# Combine all features into one matrix where each row represents a sample
# and each column represents a feature
all_features = np.hstack((feature1, feature2, feature3))

print(all_features.shape)

print(all_features)
# Output: (10, 4)

from sklearn.decomposition import PCA
# pca with Scikit-Learn

pca = PCA(n_components=3)
# pca.fit(x)

print('eigen_value', pca.explained_variance_)
print('eigen_value', pca.explained_variance_ratio_)

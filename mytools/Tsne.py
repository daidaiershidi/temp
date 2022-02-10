from sklearn.manifold import TSNE

def Tsne(X, k=2, Y=None, learning_rate='auto', init='random'):
    """
    X(N,C) -> X_embedding(N,k)
    """
    tmse = TSNE(n_components=k, learning_rate=learning_rate, init=init)
    return tmse.fit_transform(X)



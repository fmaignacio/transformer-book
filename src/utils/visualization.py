import matplotlib.pyplot as plt
import seaborn as sns

def plot_attention(attention_weights):
    plt.figure(figsize=(10, 8))
    sns.heatmap(attention_weights, annot=True)
    plt.show()

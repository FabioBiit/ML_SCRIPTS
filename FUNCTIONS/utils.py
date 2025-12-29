# DEFINISCI FUNZIONI QUI
import matplotlib.pyplot as plt
import numpy as np

def plot_test_predictions(X_vis, y_true, y_pred, feature_names, title_label):
  plt.figure(figsize=(8,6))
  markers = ['o','s','^']
  colors = ['green','blue','red']

  for idx, cl in enumerate(np.unique(y_true)):
    correct = (y_true == cl) & (y_pred == cl)
    incorrect = (y_true == cl) & (y_pred != cl)
    plt.scatter (X_vis[correct,0], X_vis[correct,1],
                 c = colors[cl], marker = markers[cl],
                 label = f"Classe {cl} - corretto", edgecolor = 'k')
    plt.scatter (X_vis[incorrect,0], X_vis[incorrect,1],
                 facecolors = 'none', marker = markers[cl],
                 label = f"Classe {cl} - errato", edgecolor = 'k', s=100)

  plt.xlabel(feature_names[0])
  plt.ylabel(feature_names[1])
  plt.title(title_label)
  plt.legend()
  plt.grid(True)
  plt.show()
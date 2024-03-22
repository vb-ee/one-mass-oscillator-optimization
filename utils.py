import matplotlib.pyplot as plt

def plot_results(datas, initial_eigens, max_N, J_pred, omo_pred, resonant_frequency, resonant_amplitude):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))

    for i in range(2):
        # Plot on the first subplot
        axs[i].scatter(
                datas[i]["J"],
                datas[i]["N"],
                color="black",
                label="Spektralpunkte filtered",
                zorder=5,
                s=10,
            )
        # color the max amplitude point red
        axs[i].scatter(
                initial_eigens[i],
                max_N[i],
                color="red",
                label="Max Amplitude",
                zorder=5,
                s=10,
            )
        
        axs[i].plot(
                J_pred[i],
                omo_pred[i],
                label="Alpha",
                color="blue",
                linewidth=1,
            )
        
        axs[i].scatter(
                resonant_frequency[i],
                resonant_amplitude[i],
                color="blue",
                label="Max Curve Fit",
                zorder=10,
                s=20,
            )
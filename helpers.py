from kaleido.scopes.plotly import PlotlyScope


def save_figure(fig_obj, fig_name):
    scope = PlotlyScope()
    with open(f"charts/{fig_name}.png", "wb") as f:
        f.write(scope.transform(fig_obj, "png"))


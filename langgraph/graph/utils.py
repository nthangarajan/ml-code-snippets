def display_graph(graph):
    from IPython.display import Image, display

    try:
        display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
    except:
        # This requires some extra dependencies and is optional
        pass
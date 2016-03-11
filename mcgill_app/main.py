import graphs
import star


def main():
    """
    Plots graph of black body emission wavelengths against amplitudes, then UBVR magnitudes of a star.
    """
    graph = graphs.FunctionsGraph(x_label="wavelength / m", y_label="amplitude")
    # Temperatures of black bodies (K) mapped to style of lines on graph.
    temps_to_styles_map = {3000.0: "g-",
                           4000.0: "b-",
                           5000.0: "r-"}
    for temp, style in temps_to_styles_map.items():
        planck_function = graphs.PlottedPlanckFunction(temp)
        graph.add_plotted_function(planck_function,
                                   style=style,
                                   label=str(int(temp)) + "K")
    graph.plot(x_range=(0.1e-6, 6e-6), point_spacing=0.02e-6)
    # TODO: input required parameters
    st = star.Star(1, 10, 4000)     # QUESTION: was unsure what temperature the star should be
    print st.get_ubvr_magnitudes()


if __name__ == "__main__":
    main()

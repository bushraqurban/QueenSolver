import streamlit as st
import plotly.graph_objects as go
from ga.algorithm import genetic_algorithm
from ga.board import draw_chessboard

st.set_page_config(page_title="QueenSolver", layout="centered")
st.subheader("Genetic Algorithm For N-Queens")

with st.sidebar:
    st.image("assets/logo.png", use_container_width=False)
    n = st.slider("Number of Queens", 4, 50, 8)
    pop_size = st.number_input("Population Size", 10, 500, 100)
    generations = st.number_input("Max Generations", 10, 5000, 1000)
    mutation_rate = st.slider("Mutation Rate", 0.0, 1.0, 0.05)
    run = st.button("Run Genetic Algorithm")

if run:
    st.write(f"Running Genetic Algorithm for **{n} Queens**...")
    solution, fitness_history, gen, solved = genetic_algorithm(n, pop_size, generations, mutation_rate)

    if solved:
        st.success(f"✅  Solution found in generation {gen}!")
    else:
        st.warning(f"⚠️ No perfect solution found in {generations} generations.")

    st.image(draw_chessboard(solution), caption="Best Solution")

    # Plot fitness
    max_fitness = n * (n - 1) // 2
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=fitness_history, mode='lines+markers',
                             line=dict(color='royalblue', width=2),
                             marker=dict(size=6), name="Fitness"))
    fig.add_shape(type="line", x0=0, x1=len(fitness_history)-1, y0=max_fitness, y1=max_fitness,
                  line=dict(color="green", dash="dash"))
    fig.add_annotation(x=0, y=max_fitness, text="Max Fitness", showarrow=False, yshift=10)
    fig.update_layout(title="Fitness Over Generations",
                      xaxis_title="Generation", yaxis_title="Fitness Score",
                      height=400, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📘  What is a Genetic Algorithm?"):
        st.markdown("""
        A **genetic algorithm** mimics natural evolution:
        - **Selection**: Pick the fittest individuals.
        - **Crossover**: Combine genes.
        - **Mutation**: Introduce variation.
        """)

    with st.expander("🧬  Fitness Function"):
        st.markdown("""
        
        The fitness function counts **non-attacking queen pairs**.
        
        Max fitness = `n*(n-1)/2`

        """ 

        f"Here, max fitness = `{max_fitness}`")

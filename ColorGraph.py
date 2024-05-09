import java.util.Arrays;

public class ColorGraph {
    private int[][] graph;
    private int[] colors;
    private int numVertices;
    private int[] solution;

    public GraphColoring(int[][] graph, int[] colors) {
        this.graph = graph;
        this.colors = colors;
        this.numVertices = graph.length;
        this.solution = new int[numVertices];
        Arrays.fill(this.solution, -1);
    }

    private boolean isSafe(int vertex, int color) {
        for (int neighbor = 0; neighbor < numVertices; neighbor++) {
            if (graph[vertex][neighbor] == 1 && solution[neighbor] == color) {
                return false;
            }
        }
        return true;
    }

    private boolean solveGraphColoring(int vertex) {
        if (vertex == numVertices) {
            return true;
        }

        for (int color : colors) {
            if (isSafe(vertex, color)) {
                solution[vertex] = color;

                if (solveGraphColoring(vertex + 1)) {
                    return true;
                }

                solution[vertex] = -1;
            }
        }

        return false;
    }

    public void solve() {
        if (solveGraphColoring(0)) {
            System.out.println("Solution exists:");
            for (int vertex = 0; vertex < numVertices; vertex++) {
                System.out.println("Vertex " + vertex + " -> Color " + solution[vertex]);
            }
        } else {
            System.out.println("No solution exists.");
        }
    }

    public static void main(String[] args) {
        int[][] graph = {
                {1, 0, 1, 0},
                {1, 0, 1, 0},
                {1, 1, 0, 1},
                {0, 1, 1, 1}
        };

        int[] colors = {1, 2, 3}; // Available colors

        GraphColoring graphColoring = new GraphColoring(graph, colors);
        graphColoring.solve();
    }
}

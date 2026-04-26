import exercise.StudentSolutionForExercise;
import exercise.StudentInformation;

import exercise.graph.Graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 * A class intended for students to implement their solutions in.
 */
public class StudentSolutionImplementation implements StudentSolutionForExercise {

    /**
     * Collects and returns information about the student working on solving the
     * instance sets.
     * This method is called automatically.
     *
     * @return First name, last name, and matriculation number collected in a
     * {@link StudentInformation} instance.
     */
    public StudentInformation provideStudentInformation() {
        return new StudentInformation(
                "Raphael", // Vorname
                "Harm", // Nachname
                "12527184" // Matrikelnummer
        );
    }

    // Implementieren Sie hier Ihre Lösung zur Zählung der Farbverstöße:
    public int countChromaticViolations(Graph G, int[] color) {
        int[][] edges = G.getEdges();
        return (int) Arrays.stream(edges)
                .filter(e -> color[e[0] - 1] == color[e[1] - 1])
                .count();
    }

    // Implementieren Sie hier Ihre Lösung der ersten Greedy-Variante:
    public int greedyMCV(Graph G, int k, int[][] colorSeq) {
        if (colorSeq == null)
            colorSeq = new int[G.numberOfVertices()][2];

        // index of current colorSeq
        int i = 0;

        int[] colorChoices = new int[G.numberOfVertices()];
        Arrays.fill(colorChoices, -1);

        for (int[] choice : colorSeq) {
            if (choice[0] == 0) {
                break;
            }
            colorChoices[choice[0] - 1] = choice[1];
            i++;
        }

        // order by degree descending, then by index
        List<Integer> q = new ArrayList<>();
        for (int v : G.getVertices())
            q.add(v);
        q.sort(Comparator.comparingInt(G::degree).reversed().thenComparingInt(Integer::intValue));

        for (int cur : q) {
            if (colorChoices[cur - 1] != -1)
                continue;

            int[] neighbors = G.getNeighbors(cur);
            int[] neighborColors = new int[k];

            // count occurrences of colors in neighbors that were already assigned
            for (int n : neighbors)
                if (colorChoices[n - 1] != -1)
                    neighborColors[colorChoices[n - 1]]++;

            // find least occurring color
            int minOccurances = Integer.MAX_VALUE, chosenColor = -1;
            for (int c = 0; c < neighborColors.length; c++) {
                if (neighborColors[c] < minOccurances) {
                    minOccurances = neighborColors[c];
                    chosenColor = c;
                }
            }

            colorSeq[i][0] = cur;
            colorSeq[i][1] = chosenColor;
            colorChoices[cur - 1] = chosenColor;
            i++;
        }

        return countChromaticViolations(G, colorChoices);
    }

    // Implementieren Sie hier Ihre Lösung der zweiten Greedy-Variante:
    public int greedyAlternativeMCV(Graph G, int k, int[][] colorSeq) {
        if (colorSeq == null)
            colorSeq = new int[G.numberOfVertices()][2];

        // index of current colorSeq
        int i = 0;

        int[] colorChoices = new int[G.numberOfVertices()];
        Arrays.fill(colorChoices, -1);

        for (int[] choice : colorSeq) {
            if (choice[0] == 0) {
                break;
            }
            colorChoices[choice[0] - 1] = choice[1];
            i++;
        }

        // order by degree descending, then by index
        List<Integer> q = new ArrayList<>();
        for (int v : G.getVertices())
            q.add(v);
        q.sort(Comparator.comparingInt(G::degree).reversed().thenComparingInt(Integer::intValue));

        for (int cur : q) {
            if (colorChoices[cur - 1] != -1)
                continue;

            int[] neighbors = G.getNeighbors(cur);
            int[] neighborColors = new int[k];

            // count occurrences of colors in neighbors that were already assigned
            for (int n : neighbors)
                if (colorChoices[n - 1] != -1)
                    neighborColors[colorChoices[n - 1]]++;

            // color with smallest index is always 0, so set it as default and find the first color without collisions
            int chosenColor = 0;
            for (int c = 0; c < neighborColors.length; c++) {
                if (neighborColors[c] == 0) {
                    chosenColor = c;
                    break;
                }
            }

            colorChoices[cur - 1] = chosenColor;
            colorSeq[i][0] = cur;
            colorSeq[i][1] = chosenColor;
            i++;
        }

        return countChromaticViolations(G, colorChoices);
    }


    // Implementieren Sie hier Ihre Lösung der dritten Greedy-Variante:
    public int greedyLookAheadMCV(Graph G, int k, int[][] colorSeq) {
        if (colorSeq == null)
            colorSeq = new int[G.numberOfVertices()][2];

        int[] colorChoices = new int[G.numberOfVertices()];
        Arrays.fill(colorChoices, -1);

        int i = 0;

        while (i < G.numberOfVertices()) {
            int min = Integer.MAX_VALUE;
            int color = -1, vertex = -1;

            for (int v : G.getVertices()) {
                if (colorChoices[v-1]!=-1)
                    continue;
                for (int c = 0; c < k; c++) {
                    colorSeq[i][0] = v;
                    colorSeq[i][1] = c;
                    int violations = greedyMCV(G, k, colorSeq);

                    // reset next two entries to stop the copy there in greedyMCV (i+2 is needed because i+1 is set in next loop)
                    colorSeq[Math.min(i + 1, colorSeq.length - 1)][0] = 0;
                    colorSeq[Math.min(i + 2, colorSeq.length - 1)][0] = 0;

                    if (violations < min) {
                        color = c;
                        vertex = v;
                        min = violations;
                    }
                }
            }

            colorChoices[vertex - 1] = color;
            colorSeq[i][0] = vertex;
            colorSeq[i][1] = color;

            i++;
        }

        return countChromaticViolations(G, colorChoices);
    }
}

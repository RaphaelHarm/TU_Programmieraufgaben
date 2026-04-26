import exercise.StudentSolutionForExercise;
import exercise.SymmetricGroup;
import java.util.ArrayList;
import java.util.List;

import exercise.StudentInformation;


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

    // Implementieren Sie hier Ihre Lösung zur Überprüfung der Korrektheit des
    // Lösungskandidaten x zum Gleichungssystem Ax = b
    public boolean isFeasible(int[][] A, int[] b, int[] x) {
        for (int i = 0; i < A.length; i++) {
            int res = 0;
            for (int j = 0; j < A[i].length; j++) {
                res += A[i][j] * x[j];
            }

            if (res != b[i])
                return false;
        }
        return true;
    }


    // Implementieren Sie hier Ihre Lösung der Fehlstände-Enumeration:
    public List<int[]> inversionStatistic(int[] permutation) {
        List<int[]> invs = new ArrayList<>();

        int[][] permCopy = new int[permutation.length][2];

        for (int i = 0; i < permutation.length; i++) {
            permCopy[i][0] = permutation[i];
            permCopy[i][1] = i;
        }

        sortAndCount(permCopy, invs);

        return invs;
    }

    private void sortAndCount(int[][] perm, List<int[]> inversions) {
        if (perm.length <= 1)
            return;

        int[][] a = new int[Math.ceilDiv(perm.length, 2)][2];
        int[][] b = new int[perm.length / 2][2];
        System.arraycopy(perm, 0, a, 0, a.length);
        System.arraycopy(perm, a.length, b, 0, b.length);

        sortAndCount(a, inversions);
        sortAndCount(b, inversions);
        mergeAndCount(a, b, perm, inversions);
    }

    private void mergeAndCount(int[][] a, int[][] b, int[][] out, List<int[]> inversions) {
        int i = 0, j = 0;
        int x = 0;

        while (i < a.length && j < b.length) {
            if (a[i][0] <= b[j][0])
                out[x] = a[i++];
            else {
                for (int i2 = i; i2 < a.length; i2++)
                    inversions.add(new int[]{a[i2][1], b[j][1]});
                out[x] = b[j++];
            }

            x++;
        }

        if (i < a.length)
            while(i < a.length) {
                out[x] = a[i];
                x++;
                i++;
            }
        else if (j < b.length)
            while (j < b.length) {
                out[x] = b[j];
                x++;
                j++;
            }
    }


    // Implementieren Sie hier die Leibniz-Formel:
    public long Leibniz(int[][] A) {
        long res = 0;
        int n = A.length;

        int[][] sg = (new SymmetricGroup(A.length)).getSymmetricGroup();

        for (int[] s : sg) {
            byte sgn = (inversionStatistic(s).size() & 1) == 0 ? (byte)1 : (byte)-1;
            long temp = 1;
            for (int i = 0; i < n; i++)
                temp *= A[i][s[i]];

            res += sgn * temp;
        }

        return res;
    }
}

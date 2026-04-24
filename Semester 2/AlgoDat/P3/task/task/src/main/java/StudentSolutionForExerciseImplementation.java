import exercise.StudentSolutionForExercise;
import exercise.StudentInformation;
import java.util.ArrayList;
import java.util.List;
import exercise.Point;
import exercise.KDNode;
import exercise.KDInnerNode;
import exercise.KDLeafNode;
import exercise.KDTree;


/**
 * A class intended for students to implement their solutions in.
 */
public class StudentSolutionForExerciseImplementation implements StudentSolutionForExercise {

    /**
     * Collects and returns information about the student working on solving the instance sets.
     * This method is called automatically.
     * @return First name, last name, and matriculation number collected in a {@link StudentInformation} instance.
     */
    public StudentInformation provideStudentInformation() {
        return new StudentInformation(
                "", // Vorname
                "", // Nachname
                "" // Matrikelnummer
        );
    }

    public void insert(Point point, KDTree tree) {
        return;
    }


    // Build the recursive Range Query here
    public Point[] computeRangeQuery(
            KDTree tree,
            double left,
            double right,
            double bottom,
            double top) {

        return null;
    }

    // Implement the naive Range Query here
    public Point[] computeRangeQueryNaive(
            List<Point> points,
            double left,
            double right,
            double bottom,
            double top) {

        return null;
    }
    
}

import exercise.Exercise;

/**
 * A task that provides an environment for students to implement their solutions in.
 */
public class Task {
    
    /**
     * Creates a {@code Task}.
     * @param args An array of arguments.
     */
    public static void main(String[] args) {

        boolean runTestMode = false;
        if (args.length > 0 && args[0].equals("--test")) {
            runTestMode = true;
        }

        Exercise exercise = new Exercise(() -> new StudentSolutionForExerciseImplementation());
        exercise.run(runTestMode);
    }
}

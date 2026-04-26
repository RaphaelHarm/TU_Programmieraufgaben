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
public class StudentSolutionImplementation implements StudentSolutionForExercise {

    /**
     * Collects and returns information about the student working on solving the instance sets.
     * This method is called automatically.
     *
     * @return First name, last name, and matriculation number collected in a {@link StudentInformation} instance.
     */
    public StudentInformation provideStudentInformation() {
        return new StudentInformation(
                "Raphael", // Vorname
                "Harm", // Nachname
                "12527184" // Matrikelnummer
        );
    }

    public void insert(Point point, KDTree tree) {
        tree.setRoot(insertRecursively(point, tree.getRoot(), 0));
    }

    private KDNode insertRecursively(Point point, KDNode node, int depth) {
        if (node == null)
            return new KDLeafNode(point);

        int axis = depth % 2;

        if (node instanceof KDLeafNode) {
            KDLeafNode leaf = (KDLeafNode) node;
            double coord;

            if (axis == 0)
                coord = (leaf.getPoint().getX() + point.getX()) / 2.0;
            else
                coord = (leaf.getPoint().getY() + point.getY()) / 2.0;

            KDNode left, right;
            if (axis == 0)
                if (point.getX() > leaf.getPoint().getX()) {
                    left = leaf;
                    right = new KDLeafNode(point);
                } else {
                    left = new KDLeafNode(point);
                    right = leaf;
                }
            else if (point.getY() > leaf.getPoint().getY()) {
                left = leaf;
                right = new KDLeafNode(point);
            } else {
                left = new KDLeafNode(point);
                right = leaf;
            }

            return new KDInnerNode(depth, coord, left, right);
        }

        KDInnerNode inner = (KDInnerNode) node;

        int comp = Double.compare(axis == 0 ? point.getX() : point.getY(), inner.getCoordinate());

        if (comp <= 0)
            inner.setLeft(insertRecursively(point, inner.getLeft(), depth + 1));
        else
            inner.setRight(insertRecursively(point, inner.getRight(), depth + 1));

        return inner;
    }


    // Build the recursive Range Query here
    public Point[] computeRangeQuery(
            KDTree tree,
            double left,
            double right,
            double bottom,
            double top) {
        var points = tree.getPoints();
        List<Point> result = new ArrayList<>();
        computeRangeQueryRecursively(tree.getRoot(), result, left, right, bottom, top);
        return result.toArray(new Point[0]);
    }

    private void computeRangeQueryRecursively(KDNode node, List<Point> result, double left, double right, double bottom, double top) {
        if (node == null)
            return;

        if (node instanceof KDLeafNode) {
            KDLeafNode leaf = (KDLeafNode) node;
            Point point = leaf.getPoint();

            if (point.getX() >= left && point.getX() <= right && point.getY() >= bottom && point.getY() <= top)
                result.add(point);
            return;
        }

        KDInnerNode inner = (KDInnerNode) node;
        int axis = inner.getDepth() % 2;

        if (axis == 0) {
            if (left <= inner.getCoordinate())
                computeRangeQueryRecursively(inner.getLeft(), result, left, right, bottom, top);
            if (right > inner.getCoordinate())
                computeRangeQueryRecursively(inner.getRight(), result, left, right, bottom, top);
        } else {
            if (bottom <= inner.getCoordinate())
                computeRangeQueryRecursively(inner.getLeft(), result, left, right, bottom, top);
            if (top > inner.getCoordinate())
                computeRangeQueryRecursively(inner.getRight(), result, left, right, bottom, top);
        }
    }

    // Implement the naive Range Query here
    public Point[] computeRangeQueryNaive(
            List<Point> points,
            double left,
            double right,
            double bottom,
            double top) {

        List<Point> result = points.stream().filter(p -> p.getX() >= left && p.getX() <= right && p.getY() >= bottom && p.getY() <= top).toList();
        return result.toArray(new Point[0]);
    }

}

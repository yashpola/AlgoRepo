package algorithms.convexhull;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class KirkPatrickSeidel {
    class Point {
        private double x;
        private double y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double getX() {
            return x;
        }

        public double getY() {
            return y;
        }

        @Override
        public boolean equals(Object other) {
            if (!(other instanceof Point)) {
                return false;
            }

            Point otherPoint = (Point) other;
            return this.x == otherPoint.getX() && this.y == otherPoint.getY();
        }

        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
    }

    public List<Point> findConvexHull(List<Point> points) {
        if (points.size() <= 1) {
            return points;
        }

        points.sort((Point pointA, Point pointB) -> {
            if (pointA.getX() > pointB.getX()) {
                return 1;
            } else if (pointA.getX() < pointB.getX()) {
                return -1;
            } else
                return 0;
        });
        Point medianX = points.get((int) Math.floor(points.size() / 2));

        List<Point> points1 = new ArrayList<>(points
                .stream()
                .filter((Point point) -> {
                    return point.getX() <= medianX.getX();
                }).toList());
        List<Point> points2 = new ArrayList<>(points
                .stream()
                .filter((Point point) -> {
                    return point.getX() > medianX.getX();
                }).toList());

        if (points2.isEmpty()) {
            return points1;
        }

        Point maxY = getPointWithMaxY(points2);

        points1 = new ArrayList<>(points1
                .stream()
                .filter((Point point) -> {
                    return point.getX() >= maxY.getX() || point.getY() >= maxY.getY();
                }).toList());
        points2 = new ArrayList<>(points2
                .stream()
                .filter((Point point) -> {
                    return point.getX() >= maxY.getX() || point.getY() >= maxY.getY() || (point.equals(maxY));
                }).toList());

        List<Point> hull1 = findConvexHull(points1);
        List<Point> hull2 = findConvexHull(points2);

        hull1.addAll(hull2);
        hull1.add(maxY);

        return hull1;
    }

    private Point getPointWithMaxY(List<Point> points) {
        Point maxY = points.get(0);

        for (Point point : points) {
            double currMaxY = maxY.getY();
            double pointY = point.getY();
            if (pointY > currMaxY)
                maxY = point;
        }

        return maxY;
    }

    public static void main(String[] args) {
        KirkPatrickSeidel sample = new KirkPatrickSeidel();

        List<Point> samplePoints = new ArrayList<>();
        samplePoints.add(sample.new Point(1, 1));
        samplePoints.add(sample.new Point(3, 3));
        samplePoints.add(sample.new Point(4, 4));
        samplePoints.add(sample.new Point(3, 7));
        samplePoints.add(sample.new Point(1, 9));
        samplePoints.add(sample.new Point(7, 5));
        samplePoints.add(sample.new Point(6, 8));
        samplePoints.add(sample.new Point(8, 7.1));
        samplePoints.add(sample.new Point(9, 4.1));
        samplePoints.add(sample.new Point(10, 1));

        Set<Point> sampleConvexHull = new HashSet<>(sample.findConvexHull(samplePoints));

        System.out.println(sampleConvexHull);
    }

}
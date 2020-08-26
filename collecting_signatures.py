# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def compute_optimal_points(segments):
    """ this function takes in a set of segments on a line
    and outputs the point markers on the line
    so that each segment contains at least one marked point and the number of points markers is the minimum
    example:
    input:
    3
    1 3
    2 5
    3 6
    output:
    1
    3
    in this sample, we have three segments: [1, 3], [2, 5], [3, 6] (of length 2, 3, 3 respectively).
    All of them contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.
    """
    sorted_segments = sorted(segments)
    output_points = []
    output_point_min = sorted_segments[0].start
    output_point_max = sorted_segments[0].end

    for segment in sorted_segments:
        if segment.start <= output_point_max:
            output_point_min = segment.start
            output_point_max = min(output_point_max, segment.end)
            continue
        else:
            output_points.append(output_point_max)
            output_point_min = segment.start
            output_point_max = segment.end

    output_points.append(output_point_max)

    return output_points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

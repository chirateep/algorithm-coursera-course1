# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def sort_segment(segment):
    return segment.start, segment.end


def optimal_points(segments):
    points = []
    segments.sort(key=sort_segment)
    i = 0
    sect_start = segments[i].start
    sect_end = segments[i].end
    while (i < len(segments)):
        s = segments[i]
        if s.start >= sect_start and s.start <= sect_end:
            sect_start = s.start
            if sect_end >= s.end:
                sect_end = s.end
        else:
            points.append(max(sect_start, sect_end))
            sect_start = s.start
            sect_end = s.end

        if i == (len(segments) - 1):
            points.append(max(sect_start, sect_end))
        i += 1
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]),
                    zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

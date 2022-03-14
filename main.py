# flake8: noqa CCR001
import logging

import log_config
import entity

logger = logging.getLogger(__name__)


def read_input(*types):
    """Read inputs according to specified types."""
    raw_line = input().strip()
    raw_inputs = raw_line.split(' ')
    return [tp(inp) for tp, inp in zip(types, raw_inputs)]


def main():
    """Run main routine."""
    plateau_points = read_input(int, int)
    plateau = entity.Plateau(entity.Point(*plateau_points))

    rovers_instructions = []
    while True:
        try:
            *initial_position, orientation = read_input(int, int, str)
            [instructions] = read_input(str)
            initial_point = entity.Point(*initial_position)
            rover = entity.Rover(plateau, initial_point, orientation)
            rovers_instructions.append([rover, instructions])
        except EOFError:
            break
    for rover, instructions in rovers_instructions:
        logger.info('rover start moving')
        rover.explore(instructions)
        print(rover.position.x, rover.position.y, rover.orientation)
        logger.info('rover finish moving')


if __name__ == '__main__':
    logger.info('Start execution')
    main()
    logger.info('End execution')

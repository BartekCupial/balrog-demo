import pygame

from balrog_demo.cfg.arguments import parse_args, parse_full_cfg
from balrog_demo.cfg.cfg import add_extra_params_demo
from balrog_demo.envs.babaisai.babaisai_params import add_extra_params_babaisai_env, babaisai_override_defaults
from balrog_demo.play import play


def parse_babaisai_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_babaisai_env(parser)
    add_extra_params_demo(parser)
    babaisai_override_defaults(partial_cfg, parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def get_action(env, play_mode, obs):
    keys_to_action = {
        (pygame.K_UP,): "up",
        (pygame.K_DOWN,): "down",
        (pygame.K_LEFT,): "left",
        (pygame.K_RIGHT,): "right",
    }
    relevant_keys = set(sum(map(list, keys_to_action.keys()), []))
    pressed_keys = []

    while True:
        # process pygame events
        for event in pygame.event.get():
            # test events, set key states
            if event.type == pygame.KEYDOWN:
                if event.key in relevant_keys:
                    pressed_keys.append(event.key)
            elif event.type == pygame.QUIT:
                return None

        action = keys_to_action.get(tuple(sorted(pressed_keys)), None)  # TODO: was 0
        pressed_keys = []

        if action is not None:
            return action

        env.render()


def main():
    cfg = parse_babaisai_args()
    play(cfg, get_action=get_action)


if __name__ == "__main__":
    main()

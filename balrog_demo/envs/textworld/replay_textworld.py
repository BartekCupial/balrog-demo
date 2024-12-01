from balrog_demo.cfg.arguments import parse_args, parse_full_cfg
from balrog_demo.cfg.cfg import add_extra_params_demo, add_extra_params_replay
from balrog_demo.envs.textworld.textworld_params import add_extra_params_textworld_env, textworld_override_defaults
from balrog_demo.legacy_replay import replay


def parse_textworld_args(argv=None):
    parser, partial_cfg = parse_args(argv=argv)
    add_extra_params_textworld_env(parser)
    add_extra_params_demo(parser)
    add_extra_params_replay(parser)
    textworld_override_defaults(partial_cfg, parser)
    final_cfg = parse_full_cfg(parser, argv)
    return final_cfg


def main():
    cfg = parse_textworld_args()
    replay(cfg)


if __name__ == "__main__":
    main()

# 0.3.0 - 12/18/2018
### Added
+ There are now Enemies, and they spawn randomly.
    + `Enemy` class added, and with it `EnemySpawner` too.
    + Enemy types are now stored in a json file.

### Changed
+ Window is slightly bigger.
+ Technical stuff.
    + The queue based system is now a bunch of hacky global variable thingy.

### Fixed
+ Projectiles are no longer "ghosts" when they hit themselves.

# [0.2.0](https://github.com/SartoRiccardo/grigorgargoyle/commit/0a9dc24061d9e51a388e04ef7d317055aecf8a19) - 12/11/2018
### Added
+ Grigor now shoots with Z.
+ Added the `Projectile` class.

### Changed
+ Now the window updates with a queue containing the `update` procedures from entities.

# [0.1.1](https://github.com/SartoRiccardo/grigorgargoyle/commit/1ebbd7174e2b55a30b95649acbac29d3ed5c0dba) - 12/08/2018
### Added
+ Window title is now "Grigor Gargoyle".

### Fixed
+ `goBack()` and `turn()` improved, now moving Grigor isn't as painful.
+ You can now choose whether an entity can or can't exit the frame.
+ Hitbox now updates when its Entity moves.

# [0.1.0](https://github.com/SartoRiccardo/grigorgargoyle/commit/73a62d019868a37092d3bb44d9f3e710495f0ef5) - 12/07/2018 - Initial Commit
### Added
+ `Entity`, `Player`, `Hitbox` and `Direction` classes are fully functional (but not complete).

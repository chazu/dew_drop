# DEW DROP ***OLD REPO***

A system for modelling complex item systems, with an eye towards modelling spaceship parts in particular

## Components / Items

## Common Simulation Elements - Item degredation

  - Input and Output are abstract properties of all components
  - Performance degredation occurs by varying the output of one component
  - Failure chance increases as quality degrades
  - Critical Failures

## Behaviors & Requirements

  - Behaviors encapsulate the state changes caused to components and/or the game environment by the utilization of an item
  - Requirements represent tests which must return true in order to execute behaviors

## Declarative Definition of Components & Items

Concrete instances of components can be declaratively specified using JSON documents:

{
  "name": "UltraDerp 5001 Mk II",
  "spec": {
    "config_dict": "goes_here"
  }
  "behaviors": [],
  "signal_handlers": [
    {
      "signal": "lol",
      "handler": "poop"
    }
  ]
}

## Items & Environments

## Future Shit

### Materials, Consumables & Repair Agents
### Forges
### Item breakdown (post-initialization)
### Tuning

  A standard API for tuning should be exposed so that different classes of items can implement different methodologies for tuning and optimizing their performance - 
  - Electrical level tweaking
  - Sequence diagram editing

### MetaQuality

  A measure of overall item quality should be developed

### Caching
### Sensors

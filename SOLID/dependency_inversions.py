"""
* Highe level classes should not depend on low level classes, it happens most of the time because
    we write low level classes first and then make the high level classes dependent on them

* Abstractions (High Level Classes) should not depend on implementations (Low level class)

Solve it using Bridge pattern or Singleton Design patterns are there to solve it

It helps in writing tests function also
Concrete business class should not depend on concreete low level class but the abstraction of those

You can do this inversion using dependency injection, parameter injection or constructor injection

this is gem: https://www.youtube.com/watch?v=S9awxA1wNNY&list=PLrhzvIcii6GMQceffIgKCRK98yTm0oolm&index=2

It can even reduce classes , if the concrete business class are very similar
"""

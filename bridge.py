"""
It separates the abstraction from implementations and they can actually grow and change independently
Eg.
like in music player
There is on home you have view of Artist, Genre, Trending ->  and their different views
resources <=> views can happen, cartesian products we have

Basically it separates the business logic (maybe anything) from the actual implementation, the similar thing is done by
strategy design pattern for dependency inversion but here we can have common implementations for different but similar
resources

Also if you have two separate classes and they are using each other then, for combinations of those classed one can use
bridge pattern, it makes easier to add or remove the new classes from both types
If you have A classes using B other classes, it reduces total number of classes you may have to write to A+B from A*B
"""
from abc import ABC, abstractmethod


class Thumbnail(ABC):
    @abstractmethod
    def get_thumbnail(self):
        pass


class SmallThumbnail(Thumbnail):
    def get_thumbnail(self):
        pass


class LargeThumbnail(Thumbnail):
    def get_thumbnail(self):
        pass


class Media(ABC):
    @abstractmethod
    def get_preview(self):
        pass


class Video(Media):
    def __init__(self, thumbnail: Thumbnail):
        self.thumbnail = thumbnail

    def get_preview(self):
        self.thumbnail.get_thumbnail()


class Image(Media):
    def __init__(self, thumbnail: Thumbnail):
        self.thumbnail = thumbnail

    def get_preview(self):
        self.thumbnail.get_thumbnail()


a = Image(SmallThumbnail()).thumbnail
b = Video(SmallThumbnail()).thumbnail

c = Image(LargeThumbnail()).thumbnail
d = Video(LargeThumbnail()).thumbnail

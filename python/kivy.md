# kivy property

user defined properties are just like regular properties that can be accessed by all the child widget and can bind action to on_properties

class properties of widget can be modified,
 but the change will not change its dependants.
  You will have to change everything manually. 
  If you use kivy properties instead, all changes will propagate to its dependencies.

# events
  
on_size(self, *args) needs to include *args even if you don't need them

# initialization  

python __init__ is run before kv file


# canvas 

Canvas instructions added in kv must be declared before child widgets.


# functions

self.collide_point(*touch.pos) checks if the touch position is within the widget.

# widget

- AsyncImage: internet image
- Carousel
- Accordion
- Slider
- CheckBox
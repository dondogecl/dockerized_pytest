# TDD Course

## Docker

See running images

	docker images

Run image

	docker compose run test sh
	
When we are inside the image we can run the command **bash** to have more command line features, such as auto-completion.


## Pytest

Run pytest using keyword

	pytest -k <test_name>

See details why a test is SKIPPED

	pytest -k <test_name> -rsx
	
### Pytest implementation

To use Context manager, import module **pytest**

	import pytest
	
To create a new test, we call the function and pass it parameters. It should not fail to pass the test. Example:

	def test_make_one_point():
		p1 = Point("Dakar", 14.7167, 17.4677)
		assert p1.get_lat_long() == (14.7167, 17.4677)
		
		
To use Context Manager and catch exception. The objective is to create an exception and catch the expected TypeException. It should throw the error, if not, it will fail the test. Example:

**test.py**

	def test_invalid_city_name():
    with pytest.raises(TypeError) as exp:
        Point(1313, 99.1234, -60.1313)
    assert str(exp.value) == "Invalid Name. It has to be a String."
	
**imported Class**

	def __init__(self, name, latitude, longitude):
	if not (isinstance(name,str)):
		raise TypeError("Invalid Name. It has to be a String.")
	self.name = name
	

## Happy Sad Path and Sad Path Testing

#### Happy path
- Organize positive cases into their own functions
- Do not mix them with negative case functions

#### Sad Path
- Negative test cases to validate against
- Two methods of handling:
	- Halt the flow of the code execution or throw an exception
	- Log that an action could not be taken and continue code execution; ideally we show show this to the user


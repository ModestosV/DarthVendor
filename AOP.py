#Copyright (c) 2005 Leo Simons
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#
# Python 2.4 metaprogramming for the rest of us -- providing java-style AOP
#

# JAVA AOP
# Example 1: java-style AOP in python

# AspectJ, AspectWerkz, ..., reduced to 8 lines of code with python...
def intercept(interceptor):
    """Python decorator that allows modification of the arguments and
       results."""
    def interceptor_generator(original_function):
        def intercept_hook(*args, **kwargs):
            return interceptor(original_function, *args, **kwargs)

        return intercept_hook
    return interceptor_generator

# here's your interceptor
def example_around_interceptor(original_function, message):
    print "before"
    result = original_function(message)
    print "after"
    print "result was: " + result
    return result

# here's an intercepted method with interception defined using
# an 'annotation'
@intercept(example_around_interceptor)
def example1(hello):
    print hello
    return hello + " world"

# Example 1a: specifiying "pointcuts" elsewhere...

# here's another method
def example1a(hello):
    print hello
    return hello + " world"

# shtuff goes here...

# in some other module, at runtime, dynamically, ..., do the equivalent of
example1a = intercept(example_around_interceptor)(example1a)


# PYTHON AOP
# Example 2: don't need no stinkin' framework...

def example_around_interceptor2(foobar):
    print "Initializing example_around_interceptor2..."

    def interceptor_generator(original_function):
        def interceptor(message):
            print "before"
            result = original_function(message)
            print "after"
            print "result was: " + result
            print "and note foobar was set to", foobar
            return result
        return interceptor
    return interceptor_generator

# here's an intercepted method with interception defined using
# an 'annotation', with configuration specified using parameters
# given to the interception function
@example_around_interceptor2("hrmpf")
def example2(hello):
    print hello
    return hello + " world"

# Python AOP, classic
# Example 3: *Really* don't need no stinkin' framework...

def example_around_interceptor3(original_function):
    def debug_calls_to_function(message):
        print "before"
        result = original_function(message)
        print "after"
        print "result was: " + result
        return result
    return debug_calls_to_function

# here's an intercepted method with interception defined using
# an 'annotation'
@example_around_interceptor3
def example3(hello):
    print hello
    return hello + " world"

# Example 3a: specifiying "pointcuts" elsewhere...
# This has been possible for *ages*...

# here's another method
def example3a(hello):
    print hello
    return hello + " world"

# shtuff goes here...

# in some other module, at runtime, dynamically, ..., do the equivalent of
example3a = example_around_interceptor3(example3a)

if __name__ == "__main__":
    print "Java like AOP..."
    example1("hello")
    example1a("hello again")
    print

    print "Python like AOP..."
    example2("hi")
    print

    print "But really, we usually don't need 'AOP', we just decorate!"
    example3("yo")
    example3a("so, ehm, functional programming rocks. Let's conquer the")
    print

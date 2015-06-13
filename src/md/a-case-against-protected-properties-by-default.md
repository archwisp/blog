# A Case Against Protected Properties By Default
For many years, it has been an accepted de-facto standard in the PHP community
to declare class properties as protected by default. The argument was
somewhere along the lines of, "If you ever need to extend this class, the
properties are accessible". I played along for a while, but my experiences
implementing the Zend framework really showed me how awful this practice can
be.

Since the developer designs the class with the idea in mind that it it can be
arbitrarily extended, little attention is given to the API. What ensues is
often implementations with very strong coupling.

To illustrate that point, lets take a look at an excerpt the Zend_Form_Element
class:

    
    
    
    class Zend_Form_Element
    {
       protected $_decorators = array();
    
       public function __construct($spec, $options = null)
       {
          $this->init();
          $this->loadDefaultDecorators();
       }
       
       public function init()
       {
       }
    
       public function loadDefaultDecorators()
       {
          if ($this->loadDefaultDecoratorsIsDisabled())
          {
             return $this;
          }
    
          $decorators = $this->getDecorators();
    
          if (empty($decorators)) 
          {
             $this->addDecorator('ViewHelper')
                ->addDecorator('Errors')
                ->addDecorator('Description', array('tag' => 'p', 'class' => 'description'))
                ->addDecorator('HtmlTag', array('tag' => 'dd', 'id'  => $this->getName() . '-element'))
                ->addDecorator('Label', array('tag' => 'dt'));
          }
    
          return $this;
       }
    }
    

Okay, so there are quite a few improvements which could be made to this code,
but thing I want to point out is that the $_decorators property is declared
protected. When the object is constructed, that property is populated by
default. The author was kind enough to to give us an option to disable to
default decorators, but it was clearly an afterthought. Why do I say that?
Because the loadDefaultDecorators() method does quite a few things! First it
checks to see if the defaults are disabled, then it builds a hierarchy of
expected objects before the HTML tags are even defined. So, if an implementor
merely wants to change the HTML tags with which the element is wrapped, all of
this code needs to be copied and pasted into an extension, just so you can
change the argument arrays. What makes this situation infinitely worse, is the
fact that this is the absolute base class. All of the form elements extend
this class. So if you want to retain the functionality of each of those form
elements, you need to extend ALL of them just to over-load the abstract
method.

If the abstract implementation needs to have features added to it later, it's
very difficult to know how others have made use of the internal structure of
the class. When you have a private property, you can check the class for
references to it and identify all of the accessors very quickly. If you need
to change the implementation of that property, you don't have to worry about
affecting implementations or extensions of the class.

The biggest problem with protected properties is the fact that you cannot
guarantee the integrity of the property.

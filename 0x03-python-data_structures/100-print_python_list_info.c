#include <Python.h>

/**
 * print_python_list_info - function prints some basic info about Python lists.
 * @p: pointer PyObject
 */

void print_python_list_info(PyObject *p)
{
    long int size;
    int i;
    PyListObject *lengthobj;

    size = PyList_Size(p);
    lengthobj = (PyListObject *)p;
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", lengthobj->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(lengthobj->ob_item[i])->tp_name);
}

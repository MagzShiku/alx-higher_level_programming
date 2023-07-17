#include <stdio.h>
#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int a;
	int i;
	int _mem;
	PyObject *_object;

	a = PyList_Size(p);
	_mem = ((PylistObject *) p)->allocated;

	printf("[*] Size of the Python List = %d\n", a);
	printf("[*] Allocated = %d\n", _mem);

	i = 0;
	while (i < a)
	{
		_obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_Type(item)->tp_name):
		i++;
	}
}

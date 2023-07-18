#define _XOPEN_SOURCE 700

#include <time.h>
#include <stdio.h>
#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int a;
	int i;
	/*Py_ssize_t _mem;*/
	PyObject *_object;
	char *buf;
	Py_ssize_t size;
	PyObject *str;

	a = PyList_Size(p);
	/*_mem*/size = ((PyListObject *) p)->allocated;

	printf("[*] Size of the Python List = %d\n", a);
	printf("[*] Allocated = %ld\n", /*_mem*/size);

	i = 0;
	while (i < a)
	{
		_object = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(_object)->tp_name);
		
		if (PyBytes_Check(_object))
		{
			printf(" Value: ");
			PyBytes_AsStringAndSize(_object, &buf, &size);
			printf("%s\n", buf);
		}
		else if (PyUnicode_Check(_object))
		{
			printf(" Value: ");
			str = PyUnicode_AsUTF8String(_object);
			/*PyObject_Print(_object, stdout, 0);*/
			printf("%s\n", PyBytes_AsString(str));
			Py_DECREF(str);
		}
		i++;
	}
}

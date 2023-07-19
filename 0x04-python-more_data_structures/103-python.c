#include <Python.h>
#include <stdio.h>
#include "lists.h"

/**
 * void print_python_list - a function that prints python list
 * p: linked list
 */

/*****Function 1 to print python lists*****/

void print_python_list(PyObject *p)
{
	PyListObject *drop_down;
	PyObject *elements;
	Py_ssize_t s, i;
	const char *variety_kind;

	printf("[*] Python list info\n");

	s = 0;
	elements = PyObject_GetIter(p);
	
	while (elements)
	{
		s++;
		elements = PyIter_Next(elements);
	}

	if ((!PyList_Check(p)))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	/*s = PyList_Size(p);*/
	printf("[*] Size of Python list = %ld\n", s);

	elements = PyObject_GetIter(p);
	drop_down = ((PyListObject * ) p);
	printf("[*] Allocated = %ld\n", drop_down->allocated);
		
	for (i = 0; i < s; i++)
	{
		elements = PyIter_Next(elements);
		if (!elements)
			break;

		variety_kind = elements->ob_type->tp_name;
		printf("Element %ld: %s\n", i, variety_kind);
	}
}

/**
 * print_python_bytes - prints infp about Python bytes objects
 * p: Paramenter
 */

/**** function that prints info on Python bytes objects.****/
void print_python_bytes(PyObject *p)
{
	const char *c;
	Py_ssize_t i;
	Py_ssize_t s;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [Error] Invalid Bytes Objects\n");
		return;
	}

	/*c = PyBytes_AsString(p);
	s = PyBytes_Size(p);*/

	c = ((PyBytesObject *)p)->ob_sval;
	s = ((PyVarObject *)p)->ob_size;

	printf(" size: %ld\n", s);
	printf(" trying string: %.*s\n", (int)s, c);
	printf(" first %ld bytes: ", s > 10 ? 10 : s);

	for (i = 0; i < (s > 10 ? 10: s); i++)
	{
		printf("%02hhx", c[i]);
		if (i < (s > 10 ? 9: s - 1))
		{
			printf(" ");
		}
	}
	printf("\n");
}

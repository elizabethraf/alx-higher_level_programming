#include "Python.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, idx = 0;
	PyObject *element;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size_p = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
		}
	}
}

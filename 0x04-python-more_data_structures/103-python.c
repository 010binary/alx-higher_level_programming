#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - prints info about Python bytes (hexa ascii)
* @p: Python Object
* Return: void
*/

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *obj;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

/**
* print_python_list_info - prints info about Python lists
* @p: Python Object
* Return: void
*/

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", str[i] & 0xff);
        if (i < 9 && i + 1 < size)
            printf(" ");
    }
    printf("\n");
}


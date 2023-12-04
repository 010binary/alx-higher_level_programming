#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int arr[1000];
	int i = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}

	i--;
	for (j = 0; j < i; j++, i--)
	{
		if (arr[j] != arr[i])
			return (0);
	}

	return (1);
}

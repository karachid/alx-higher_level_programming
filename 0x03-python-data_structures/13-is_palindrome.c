#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is palindrome
 * @head: pointer to the linked list head
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arr = NULL, s = 1, i, j;

	while (current != NULL)
	{
		arr = realloc(arr, s * sizeof(int));
		arr[s - 1] = current->n;
		current = current->next;
		s++;
	}

	for (i = 0, j = s - 2; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}

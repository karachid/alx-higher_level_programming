#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is palindrome
 * @head: pointer to the linked list head
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arr = NULL, s = 0, i, j;

	while (current != NULL)
	{
		current = current->next;
		s++;
	}

	arr = malloc(s * sizeof(int));

	i = 0;
	current = *head;

	while (current)
	{
		arr[i++] = current->n;
		current = current->next;
	}

	for (i = 0, j = s - 1; i < j; i++, j--)
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

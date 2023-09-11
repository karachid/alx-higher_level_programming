#include "lists.h"

/**
 * get_size - returns the size of the linked list
 * @head: head of the linked list
 * Return: int (size of the linked list)
 */
int get_size(listint_t **head)
{
	int s = 0;
	listint_t *c = *head;

	while (c)
	{
		c = c->next;
		s++;
	}
	return (s);
}

/**
 * reverse_list - reverses a linked list
 * @head: head of the linked list
 * Return: new head of the linked list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *prevnode = NULL, *nextnode = NULL;

	while (current)
	{
		nextnode = current->next;
		current->next = prevnode;
		prevnode = current;
		current = nextnode;	
	}
	return (prevnode);
}

/**
 * is_palindrome - checks whether a linked list is palindrome
 * @head: pointer to the linked list head
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *secondhalf = NULL, *firsthalf = *head;
	int s = 0, mid = 0, i;

	s = get_size(&current);

	if (s % 2 == 0)
		mid = s / 2;
	else
		mid = (s + 1) / 2;

	for (i = 0; i < mid; i++)
		current = current->next;

	secondhalf = reverse_list(&current);

	while(secondhalf)
	{
		if (secondhalf->n == firsthalf->n)
		{
			firsthalf = firsthalf->next;
			secondhalf = secondhalf->next;
		}
		else
			return (0);
	}

	return (1);
}

#include "lists.h"
/**
 * is_palindrome - checks code
 * @head: head of palindrome
 * Return: 0 if not, 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	size_t  *i;

	if (head == NULL|| *head == NULL)
		return (1);

	i = *head;
	while (i) /* get len of list */
	{
		i = i->next;
		len++;
	}
	return (0);
}

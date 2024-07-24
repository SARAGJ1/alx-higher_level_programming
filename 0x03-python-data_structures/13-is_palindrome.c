#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */

int is_palindrome(listint_t **head) {
	listint_t *current;
	listint_t *current1;

	if (*head == NULL)
		return (1);

	current = *head;
	current1 = NULL;
	while (current != NULL) {
		listint_t *new;
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (0);
		new->n = current->n;
		new->next = current1;
		current1 = new;
		current = current->next;
	}
	current = *head;
	while (current->next != NULL) {
		if (current1->n != current->n)
			return (0);
		current1 = current1->next;
		current = current->next;
	}
	return (1);
}

# Sample Requirement — Customer Profile API

> Synthetic example for skill validation. No real endpoint or customer data.

## User story
As an authenticated customer, I want to retrieve my own profile so that I can review my account details.

## Acceptance criteria
- AC-01: An authenticated customer can retrieve their own profile.
- AC-02: The response contains `customerId`, `displayName` and `email`.
- AC-03: An unauthenticated request is rejected with the API's documented authentication error.
- AC-04: A customer cannot retrieve another customer's profile by changing the identifier.
- AC-05: An unknown customer identifier returns the documented not-found response.
- AC-06: Sensitive internal fields are not returned.

## Notes
- HTTP method, route, exact status codes and schema are intentionally unspecified.
- Ask for the API contract before asserting exact status codes or payload details.
- Use synthetic test accounts in an explicitly authorized test environment.

# Intern Coding Challenge Instructions

## Intro

This coding challenge is designed to help us see how you approach a real-world problem using clear, maintainable code. Although you're at the start of your career, we’re interested in your problem-solving abilities, code quality, and how you structure your solution. Remember, there is no penalty for asking questions if anything is unclear.

> **Before you start:**
>
> - Feel free to use resources such as Google, StackOverflow, or any other reference you normally use.
> - If you have any questions or ideas that might help you or us better understand your approach, please ask.
> - We understand that finishing everything in one go might be challenging. It’s okay if you don’t complete every part of the challenge.
> - You will have the opportunity to discuss your solution and any incomplete parts with our team.

## Task Overview

You are provided with a starter FastAPI application that includes a Makefile entrypoint. Your tasks for this challenge are as follows:

1. **Implement a `/proxy` Endpoint:**
   - Add a new GET endpoint at `/proxy` that accepts a query parameter named `url`.
   - This endpoint should check whether the given URL has an archive available (using logic similar to that in the `/archive` endpoint).
   - **If an archive is found:** Redirect the user to the archived URL.
   - **If no archive is available:** Return a meaningful error message along with an appropriate HTTP error code.

2. **Enhance the Makefile Testing:**
   - Update the `make tests` target in the Makefile.
   - The updated test logic should verify that both the `/archive` and `/proxy` endpoints work as expected by testing them with known inputs.
   - For example, you might test:
     - That `/archive` returns the expected archive URL for a known input.
     - That `/proxy` either redirects correctly for an archived URL or returns an error message for a URL with no archive.

## How to Run and Test Your Application

- **Starting the Server:**
  - You can start the FastAPI server by simply running:
    ```sh
    make
    ```
  - This command will start the server using the default target in the Makefile.

- **Running Tests:**
  - To run the tests for both endpoints, execute:
    ```sh
    make tests
    ```
  - This target should run a suite of tests to verify the functionality of the `/archive` and `/proxy` endpoints against known inputs.

## Guidelines

- **Coding Style:**
  - Ensure your code is clean, readable, and maintainable.
  - Use meaningful variable and function names.
  - Include docstrings and comments where appropriate.

- **Functionality:**
  - Ensure that both endpoints handle errors gracefully.
  - Maintain data integrity, and when applicable, include useful context (e.g., timestamps or identifiers) in your responses.

- **Usage of Starter Code:**
  - The starter code includes a FastAPI app with a Makefile entrypoint. Build on this existing code rather than restructuring it unless necessary.
  - Keep your changes focused on implementing the required functionality.

- **Testing:**
  - Your tests should be runnable with a single command (`make tests`) and verify the functionality of both endpoints using known inputs.
  - Ensure that the tests provide clear output indicating whether the expected results were achieved.

## Submission

When you have completed the challenge:

- **Submit your work by opening a pull request on the repository.**
- Include a clear description of the changes made and any additional notes you’d like to share.
- Make sure your pull request is well-organized so that it can be easily reviewed.

## What Happens Next?

After you open your pull request, our team will review your code. We will evaluate your solution based on:
- How you approached the problem.
- Code quality and adherence to best practices.
- The effectiveness of your tests.
- Your ability to handle errors and unexpected inputs.

We look forward to discussing your work in a follow-up conversation. Good luck and happy coding!

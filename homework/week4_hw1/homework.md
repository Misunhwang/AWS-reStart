1. Convert 'client = TestClient' into a test fixture to run with a fresh instance of the app for each new test case

2. Use @pytest.mark.parameterize to test your GET API, in different scenario where you get 200 or 404 codes

3. Add another input for @pytest.mark.parameterize to compare GET response json payload
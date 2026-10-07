
def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={"Accept": "application/json",
                            "X-Api-Key": "reqres-free-v1"}
    )
    
    
    
    
    response = request.get("https://reqres.in/api/users?page=2")
    
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["data"][2]["first_name"] == "Tobias"
    assert json_data["data"][4]["last_name"] == "Edwards"
    
    request.dispose()
    print("API GET request test completed successfully.")
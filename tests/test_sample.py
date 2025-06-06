import allure

@allure.title("Test passes")
@allure.description("Always pass")
def test_pass():
  assert True

@allure.title("Test fails")
@allure.description("always fail")
def test_fail():
  assert False, "Intentional failure"
  
@allure.title("Test with steps")
@allure.description("Allure steps")
def test_with_steps():
  with allure.step("Step 1: Setup"):
    x = 1
    y = 2
  with allure.step("Step 2: Execute"):
    result = x + y
  with allure.step("Step 3: Assert"):
    assert result == 3


def PrintCurrentCategories(categoryList):
    i = 1
    for category in categoryList:
        print("{}\t{}".format(i, category))
        i = i+1


def PromptForNewCategory(categoryManager):
    categories = categoryManager.getCategoryNames()
    print("Your currently configured Categories are:")
    PrintCurrentCategories(categories)
    return input("Please enter another desired Category:\n:")


def PromptSelectCategory(categoryManager):
    categories = categoryManager.getCategoryNames()
    print("Please select a category:")
    PrintCurrentCategories(categories)
    selection = input("Enter Number:")
    selection = int(selection)
    if selection <= len(categories):
        return categories[selection-1]
    return None


def PromptCategoryRegexRelation(categoryManager, regex):
    print("Which Category does this regex belong to? {}".format(regex))
    category = PromptSelectCategory(categoryManager)
    if category is None:
        categoryManager.addRegexToCategory("Unknown", regex)
    else:
        categoryManager.addRegexToCategory(category, regex)

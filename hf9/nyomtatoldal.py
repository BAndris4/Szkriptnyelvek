def oldalak(s):
    li = s.split(",")
    result = []
    for page in li:
        if "-" in page:
            start = int(page.split("-")[0])
            end = int(page.split("-")[1])
            result.extend([str(num) for num in range(start, end + 1)])
        else:
            result.append(page)
    return ", ".join(result)


def main():
    print(oldalak("1-4,7,9,11-15"))


"#################################################################################"

if __name__ == "__main__":
    main()

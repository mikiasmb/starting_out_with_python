def main():
    name = input("Enter your name: ")
    desc = input("Describe yourself: ")
    file = open("web.html", "w")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("\t<center>\n")
    file.write(f"\t\t<h1>{name}</h1>\n")
    file.write("\t</center>\n")
    file.write("\t<hr />\n")
    file.write(f"\t{desc}\n")
    file.write("</body>\n")
    file.write("</html>\n")
    file.close()


if __name__ == '__main__':
    main()

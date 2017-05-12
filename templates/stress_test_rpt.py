from jinja2 import Environment, PackageLoader, select_autoescape


def render_report(template_path, report_path, opts, **kwargs):
    """
    
    :param kwargs: should  
    :return: 
    """
    env = Environment(
        loader=PackageLoader("./", 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('stress_test_rpt.html')
    rendered_report = template.render(**kwargs)

    try:
        with open(report_path, "wb") as writefile:
            writefile.write(rendered_report)
    except:
        print("Error writing report")
